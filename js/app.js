const api = 'https://tweetifybeats.herokuapp.com/';
console.log('hello');
const username = document.querySelector(".user-input");
const search = document.querySelector(".site-btn");
const node = document.querySelector(".tweet_container");

function getResult(e){
    e.preventDefault()
    
    if(e.keyCode == 13){
        alert('hello')
        fetch(`${api}`+username.value).then(response => response.json()).then(dataDisplay)    ;
    }
}


function dataDisplay (res){
    console.log(res[1]);
    console.log(res[2]);
    console.log(res[3]);
    console.log(res["user"]);
    // 
    
    list = document.createElement('div');
    list.classList.add("row");
    list.innerHTML = `
  <div class="col-lg-6">
			  <div class="section-title">
				<h2 class="user_name">${res["user"]}</h2>
			  </div>
			</div>
			<div class="col-lg-6">
			  <p class="user_tweet">
				${res[1]}
			  </p>
			  <button>Guitar</button>
			  <button>Piano</button>
			  <button>Xylophone</button>
			</div>`
    node.appendChild(list)
}

username.addEventListener('keypress', getResult);

search.addEventListener('onClick', (e)=>{
    e.preventDefault();
    alert('hello')
})








