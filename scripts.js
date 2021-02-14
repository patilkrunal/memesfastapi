const app = document.getElementById('root');
const container = document.createElement('div');
container.setAttribute('class', 'container');

app.appendChild(container);
const URL = "https://memefastapi.herokuapp.com/meme/";
// const URL = "http://127.0.0.1:8000/meme/";

// GET REQUEST
var request = new XMLHttpRequest();
request.open('GET', URL);

request.onload = function () {
  var data = JSON.parse(this.response);
  if (request.status >= 200 && request.status < 400) {
    data.data[0].forEach(meme => {
//       console.log('meme', meme)
      const card = document.createElement('div');
      card.setAttribute('class', 'card');

      const h1 = document.createElement('h1');
      h1.textContent = meme.user;

      const img = document.createElement('img');
      img.src = meme.url;
      
      const h4 = document.createElement('h4');
      h4.textContent = meme.caption;

      container.appendChild(card);
      card.appendChild(h1);
      card.appendChild(img);
      card.appendChild(h4);
    });
  }
   else {
    const errorMessage = document.createElement('marquee');
    errorMessage.textContent = `Gah, it's not working!`;
    app.appendChild(errorMessage);
  }
}

request.send();


var form = document.getElementById("myform");

form.addEventListener( "submit", (event) => {
  event.preventDefault();
  var request = new XMLHttpRequest();
  
  request.open("POST", URL, true);
  request.setRequestHeader("Content-Type", "application/json");
  request.onreadystatechange = function () {
    if (request.readyState === 4 && request.status >= 200 && request.status < 400) {
      var json = JSON.parse(request.responseText);
      alert("Meme uploaded successfully.");
    }
  };

  var data = JSON.stringify({
    "user": document.getElementById("user").value, 
    "url": document.getElementById("url").value,
    "caption": document.getElementById("caption").value
  });
  request.send(data);  
});
