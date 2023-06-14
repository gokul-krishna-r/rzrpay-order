import razorpay
from fastapi import FastAPI
from fastapi import Body
from fastapi.middleware.cors import CORSMiddleware
import os,base64,io

app = FastAPI(
    title="Razor Pay API",
    version="0.5.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


RZR_KEY_SECRET= os.environ.get('RZR_KEY_SECRET')
RZR_KEY_ID=os.environ.get('RZR_KEY_ID')

razorpay_client = razorpay.Client(auth=(RZR_KEY_ID, RZR_KEY_SECRET))
razorpay_client.set_app_details({"title" : "IMA MSN", "version" : "0.5.0"})

@app.get("/",tags=["Test"])
async def test_response():
    return "Api Start"

@app.post("/order")
async def create_order(amount=Body(title="amount")):
    data = { "amount": amount, "currency": "INR"}
    payment = razorpay_client.order.create(data=data)
    return payment


