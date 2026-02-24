const http=require("http")
let a={"name":"shailesh"}
http.createServer((req,res)=>{
    if(req.url=="/home"){
        res.write("home")
        res.end()
    }
    else{
        res.writeHead(200,{"content-type":"application/json"});        
        res.write({"name":"shailesh"})
        res.end()
    }
    
    
}).listen(3000)