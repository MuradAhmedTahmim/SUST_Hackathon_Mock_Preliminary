from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .classifier import classify_ticket

@api_view(["GET"])
def health(request):
    return Response({
        "status": "ok"
    })

@api_view(["POST"])
def sort_ticket(request):

    ticket_id = request.data.get("ticket_id")
    message = request.data.get("message")

    if not ticket_id:
        return Response(
            {"error": "ticket_id is required"},
            status=400
        )

    if not message:
        return Response(
            {"error": "message is required"},
            status=400
        )

    result = classify_ticket(message)

    return Response({
        "ticket_id": ticket_id,
        **result
    })