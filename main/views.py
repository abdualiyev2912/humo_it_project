from typing import Any
import asyncio
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View
from main.models import *
from telegram import Bot


TELEGRAM_BOT_TOKEN = '7504207747:AAF-NJIWiWc53B_HV54PJCpGkHjO7YbwvlI'
TELEGRAM_CHAT_ID = '6956977079'


class PortfolioMainView(View):
    def get(self, request):
        return render(request, 'index.html', {
            "developers": Developer.objects.order_by('-experience')[:6],
            "portfolios": Portfolio.objects.all()[:3],
            "news": New.objects.all()[:3],
            "comments": Comment.objects.order_by("-created_at")[:3],
        })

    @staticmethod
    async def send_message(contact: Contact):
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        telegram_message = (
            f"Yangi Kontakt:\n"
            f"Ism: {contact.name}\n"
            f"Email: {contact.email}\n"
            f"Mavzu: {contact.subject}\n"
            f"Xabar: {contact.message}"
        )
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=telegram_message)

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            contact = Contact.objects.create(name=name, email=email, subject=subject, message=message)
            
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self.send_message(contact))
            loop.close()

            return redirect('main')
        else:
            messages.error(request, "Iltimos, maydonlarni to'ldiring!")
            return render(request, 'index.html', {
                "developers": Developer.objects.order_by('-experience')[:6],
                "portfolios": Portfolio.objects.all()[:3],
                "news": New.objects.all()[:3],
                "comments": Comment.objects.order_by("-created_at")[:3],
            })
