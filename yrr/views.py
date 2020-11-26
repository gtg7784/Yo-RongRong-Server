import io
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import PIL.Image as Image
from .models import Img, Log
from .ai import CompareImg


@csrf_exempt
def index(req):
    return HttpResponse("index")


@csrf_exempt
def getResult(req):
    phone_id = req.body.get("phone_id")
    image_bytes = req.body.get("image")
    print(image_bytes)

    image = Image.open(io.BytesIO(image_bytes))

    model = Log(phone_id=phone_id, image=image)
    model.save()

    imgs = [i.image for i in Img.objects.all()]
    names = [i.product_name for i in Img.objects.all()]

    cmp = CompareImg(image, imgs)

    idx = cmp.compare()

    res = {
        "image": imgs[idx],
        "product_name": names[idx],
        "simillarity": cmp.percentage
    }

    return JsonResponse(res)

@csrf_exempt
def getAllProducts(req):
    phone_id = req.body.get("phone_id")
    objs = Log.objects.filter(phone_id=phone_id)

    print(objs)

    return JsonResponse({"status": 200})

