from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/armstrong/<int:n>')
def arm(n):  

    sum=0
    order=len(str(n))
    copy_n=n
    while(n>0):
        digit=n%10
        sum+=digit**order
        n=n//10
    if(sum==copy_n):
        print(f"{copy_n} is an armstrong no.")
        result={
            "Number":copy_n,
            "Seriver IP": "125.521.145",
            "Armstrong": True,
            "Others Numbers":[1,5,22,52]
            }
  
    else:
       print(f"{copy_n} is not an armstrong no.")  
       result={
            "Number":copy_n,
            "Seriver IP": "125.521.145",
            "Armstrong": False,
            "Others Numbers":[1,5,22,52]

             }   

    return(jsonify(result))           
       

if __name__=="__main__":
  app.run(debug=True)