from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import google.generativeai as genai
from django.conf import settings
import json

def ai_chat(request):
    return render(request, 'ai_service/chat.html')

@csrf_exempt
def ai_chat_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message', '')
            
            if not message:
                return JsonResponse({'error': 'No message provided'}, status=400)
            
            if not settings.GEMINI_API_KEY:
                return JsonResponse({
                    'response': 'AI service is not configured. Please add your Gemini API key to use this feature.'
                })
            
            genai.configure(api_key=settings.GEMINI_API_KEY)
            model = genai.GenerativeModel('gemini-pro')
            
            prompt = f"""You are an AI assistant for Igbo Archives, a cultural preservation platform. 
            Help users with questions about Igbo culture, history, and heritage.
            
            User question: {message}"""
            
            response = model.generate_content(prompt)
            
            return JsonResponse({
                'response': response.text
            })
            
        except Exception as e:
            return JsonResponse({
                'response': f'I apologize, but I encountered an error: {str(e)}'
            })
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)
