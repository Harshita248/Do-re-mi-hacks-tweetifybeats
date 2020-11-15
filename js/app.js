const api = 'https://tweetifybeats.herokuapp.com/'
const local="http://localhost:5000/"




let username;
// const search = document.querySelector(".site-btn");
const node = document.querySelector(".tweet_container");
// const hs =document.querySelector('.hs-text')

function getResult(username){
    // console.log(e);
    // e.preventDefault()
    
    // if(e.keyCode == 13){
        console.log('hello');
        // alert('hello')
        fetch(`${api}${username}`).then(response => response.json()).then(dataDisplay)    ;
    }
// }

function dataDisplay (res){
    // console.log(res[1]);
    // console.log(res[2]);
    // console.log(res[3]);
    // console.log(res["user"]);
    //
    console.log(res); 
    let list;
    
    for(let i = 1; i<=3; i++){
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
                    ${res[i]}
                  </p>
                  <button onclick="fetch('${local}${username}'+'/'+${i}+'/guitar');">Guitar</button>
                  <button onclick="fetch('${local}${username}'+'/'+${i}+'/piano');">Piano</button>
                  <button onclick="fetch('${local}${username}'+'/'+${i}+'/xylophone');">Xylophone</button>
                </div>`
                node.appendChild(list)
    }
}

// window.addEventListener('DOMContentLoaded', () => {
// username.addEventListener('keypress', () => {
//     console.log('hey');
// });

// // search.onclick = () =>{
// //     alert('hello')
// // }

// search.addEventListener('click', () => {
//     console.log('hey');
// })
// console.log(hs);
// })



const handleKeyPress = (e) => {
    username = e.value
}

const handleClick = () => {
    getResult(username)
}






