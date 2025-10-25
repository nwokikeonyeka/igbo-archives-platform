from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
import google.generativeai as genai
from django.conf import settings
import json


def ai_chat(request):
    """Main AI chat interface"""
    return render(request, 'ai_service/chat.html')


@require_http_methods(["POST"])
def ai_chat_api(request):
    """Handle AI chat messages using Gemini API"""
    try:
        # Get message from request
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            message = data.get('message', '')
        else:
            message = request.POST.get('message', '')
        
        if not message:
            if request.headers.get('HX-Request'):
                return HttpResponse('<div class="ai-message error">Please enter a message.</div>')
            return JsonResponse({'error': 'No message provided'}, status=400)
        
        # Check if API key is configured
        if not settings.GEMINI_API_KEY:
            response_html = '''
            <div class="ai-message error">
                <i class="fas fa-exclamation-circle"></i>
                AI service is not configured. Please contact the administrator to add a Gemini API key.
            </div>
            '''
            if request.headers.get('HX-Request'):
                return HttpResponse(response_html)
            return JsonResponse({
                'response': 'AI service is not configured. Please add your Gemini API key to use this feature.'
            })
        
        # Configure and call Gemini API
        genai.configure(api_key=settings.GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        
        # Enhanced system prompt for better Igbo cultural context
        prompt = f"""You are an AI assistant for Igbo Archives, a digital platform dedicated to preserving and celebrating Igbo culture, history, and heritage.

Your role:
- Provide accurate, respectful information about Igbo culture, traditions, history, and language
- Help users explore the rich heritage of the Igbo people
- Answer questions about artifacts, customs, festivals, and cultural practices
- Encourage cultural preservation and learning
- Be concise but informative in your responses

User question: {message}

Please provide a helpful, culturally sensitive response."""
        
        response = model.generate_content(prompt)
        
        # Format response for HTMX
        if request.headers.get('HX-Request'):
            response_html = f'''
            <div class="user-message">
                <div class="message-content">{message}</div>
            </div>
            <div class="ai-message">
                <i class="fas fa-robot"></i>
                <div class="message-content">{response.text}</div>
            </div>
            '''
            return HttpResponse(response_html)
        
        # JSON response for non-HTMX requests
        return JsonResponse({'response': response.text})
        
    except Exception as e:
        error_message = f'I apologize, but I encountered an error: {str(e)}'
        if request.headers.get('HX-Request'):
            return HttpResponse(f'<div class="ai-message error"><i class="fas fa-exclamation-triangle"></i> {error_message}</div>')
        return JsonResponse({'error': error_message}, status=500)
