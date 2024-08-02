#!/usr/bin/python3
import jetson_inference
import jetson_utils
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="Path of the image to process")
opt = parser.parse_args()
img = jetson_utils.loadImage(opt.filename)
net = jetson_inference.imageNet(model="spiders.onnx",labels="labels.txt",input_blob="input_0", output_blob="output_0")
class_idx, confidence = net.Classify(img)
class_desc = net.GetClassDesc(class_idx)
print("This person is feeling "+ str(class_desc).lower() +" (class #"+ str(class_idx) +") with a" + str(confidence*100)+"% confidence")

if class_desc == 'Bean':
    print("An edible seed, typically kidney-shaped, growing in long pods on certain leguminous plants.")
elif class_desc == 'Bitter_Gourd':
    print("A rough-skinned, green-colored unripe fruit used in Asian cooking and for its medicinal properties.")
elif class_desc == 'Bottle_Gourd':
    print("A common cultivated gourd (Lagenaria siceraria) having a variably shaped fruit with a hard shell that is sometimes used as a container.")
elif class_desc == 'Brinjal':
    print("Also known as eggplant, aubergine, or baigan; brinjal is a plant species in the nightshade family Solanaceae.")
elif class_desc == 'Broccoli':
    print("A cultivated variety of cabbage bearing heads of green or purplish flower buds that are eaten as a vegetable.")
elif class_desc == 'Cabbage':
    print("A cultivated plant eaten as a vegetable, having thick green or purple leaves surrounding a spherical heart or head of young leaves.")
elif class_desc == 'Capsicum':
    print("A tropical American pepper plant of the nightshade family with fruits containing many seeds. Many cultivated varieties with edible, pungent fruits have been developed.")
elif class_desc == 'Carrot':
    print("A  tapering orange-colored root eaten as a vegetable.")
elif class_desc == 'Cauliflower':
    print("A cabbage of a variety which bears a large immature flower head of small creamy-white flower buds.")
elif class_desc == 'Cucumber':
    print("A long, green-skinned fruit with watery flesh, usually eaten raw in salads or pickled.")
elif class_desc == 'Papaya':
    print("A tropical fruit shaped like an elongated melon, with edible orange flesh and small black seeds.")
elif class_desc == 'Potato':
    print("A starchy plant tuber which is one of the most important food crops, cooked and eaten as a vegetable.")
elif class_desc == 'Pumkin':
    print("A large rounded orange-yellow fruit with a thick rind, edible flesh, and many seeds.")
elif class_desc == 'Radish':
    print("A swollen pungent-tasting edible root, especially a variety which is small, spherical, and red, and eaten raw with salad.")
elif class_desc == 'Tomato':
    print("A glossy red, or occasionally yellow, pulpy edible fruit that is eaten as a vegetable or in salad.")
