import os
import pandas
from api.neuron_model import ResNetUltra
from backend.settings import BASE_DIR
from core.models import ResNet, Category, CategorySpecific

path = os.path.join(BASE_DIR, 'hakaton')
resnet = ResNetUltra()
import pandas as pd

idArray = []
predictions1 = []

for item in range(232):
    idArray.append(item + 1)
    category_name = resnet.netPredict(model=ResNet.objects.last(),
                                      gimage=f"{path}/{item + 1}.jpg"
                                      )
    category = Category.objects.filter(category__contains=category_name).first()
    if category is None:
        specific = CategorySpecific.objects.filter(category__contains=category_name).first()
        category = specific.parent
    predictions1.append(category)

dict = {'id': idArray, 'prediction': predictions1}

df = pd.DataFrame(dict)
print("SAVED")
df.to_csv("result.csv")
