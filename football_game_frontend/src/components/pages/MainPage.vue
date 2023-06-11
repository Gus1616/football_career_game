<template>
    <div>
        <button class="nav">
            <router-link to="/">Home</router-link>
        </button>
    <h1>Guess the Player</h1>
    </div>
    <input placeholder="enter player name..." />

    <div class="timer">Timer: {{ countDown }} </div>

    <div class="container">
  <div class="square">
    {{ gareth }}
  </div>
  

</div>
<div>
    <a class="back" href="#">&laquo; Back</a>
    <a class="back" href="#">Next &raquo;</a>
</div>


</template>

<script>

import axios from 'axios';


 export default {
        data () {
            return {
                countDown: 90,
                gareth: null
            }
        },
        methods: {
            countDownTimer () {
                if (this.countDown > 0) {
                    setTimeout(() => {
                        this.countDown -= 1
                        this.countDownTimer()
                    }, 1000)
                }
                if (this.countDown==0){
                    this.$router.push('/')
                }
            }
        },
        created () {
            this.countDownTimer(),
            axios.get('http://localhost:8000/careerApp/load-json/')
            .then(response => {
                // this.message = response.data.message;
                console.log("hello"+ response.data.data.Gareth_Barry)
                this.gareth = response.data.data.Gareth_Barry
            })
            .catch(error => {
                console.error(error);
            });
                    
        }
    }


</script>


<style>
.back{
   text-decoration: none;
   color: white;
   background: #dc3545;
   padding: 7px 10px;
   border-radius: 4px;  
   font-size: 19px;
   margin-right: 3px;

}
.back:hover{
   background: rgb(220 53 69 / 85%);
}
.back:focus{
    outline: 3px solid rgb(220 53 69 / 50%);
   
}

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 60vh;
}

.square {
    /* display: flex;
  justify-content: center;
  align-items: center;
  margin-left: 45%; */
    width: 250px;
    height: 350px;
    border: 3px solid black;
    border-radius: 10px 10px 10px 10px;


}

.timer {
  position: absolute;
  top: 5%;
  right: 5px;
  font-size: 30px;
  color: crimson;
  border: 4px solid red;

}


.nav {
  background-color: white;
  color: black;
  border: 2px solid #4CAF50; /* Green */
  margin-top: 20px;
}
.nav:hover {
  box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19);
}

</style>