import math

###Functions###
def sigmoid(x):
    return 1 / (1 + math.exp(-x))
def sigmoidd(x):
    return sigmoid(x)*(1-sigmoid(x))
def forward_pass(node,weight,bias):
    return sigmoid(node*weight+bias)
def error_function(y,yhat):#predicted value is yhat
    return 1/2*(y-yhat)**2
###Initilization###
layer1_node1 = 0.3
weight_1 = 1
bias_1 = 0
weight_2 = -1
bias_2 = 0
y = 0.2
nodes = [[0]]#nodes[layer][node]

print(forward_pass(forward_pass(layer1_node1,weight_1,bias_1),weight_2,bias_2))

for i in range(100000):
    if(i%2 == 0):
        layer1_node1 = 0.6
        y = 0.5
    else:
        layer1_node1 = 0.3
        y=0.2
    #do forward propogation
    layer_1_out = forward_pass(layer1_node1,weight_1,bias_1)
    layer_2_out = forward_pass(layer_1_out,weight_2,bias_2)
    
    #back propagation for layer 1
    error = layer_2_out-y#1
    partial_2 = sigmoidd(layer_1_out*weight_2+bias_2)#2 partial derivative for layer 2
    adjust_weight_2 = error*partial_2*layer_1_out
    adjust_bias_2 = error*partial_2
    
    #back propagation for layer 2
    partial_1 = sigmoidd(layer1_node1*weight_1+bias_1)
    total_derivative = error*partial_2*weight_2*partial_1*layer1_node1
    adjust_bias_1 = error*partial_2*partial_1*weight_2
    
    weight_2 = weight_2 - (adjust_weight_2)
    weight_1 = weight_1 - (total_derivative)
    bias_2 = bias_2 - adjust_bias_2
    bias_1 = bias_1 - adjust_bias_1
    
a = 0#(error_function(forward_pass(forward_pass(0.3,weight_1,bias_1),weight_2,bias_2),0.2))
#print(weight_2)
#print(error,partial_2,layer_1_out)
print("Prediction: "+str(forward_pass(forward_pass(0.6,weight_1,bias_1),weight_2,bias_2)))
print("IT SHOULD BE 0.5")
print("Prediction: "+str(forward_pass(forward_pass(0.3,weight_1,bias_1),weight_2,bias_2)))
print("IT SHOULD BE 0.2")
print("100000 iterations")
#print("Total: "+ str(a+b))

#print(error_function(y,forward_pass(layer1_node1,weight,bias)))