<template>
    <div>
        <button class="nav">
            <router-link style="   text-decoration: none;" to="/">Home</router-link>
        </button>
    <h1>Guess the Player</h1>
    </div>
    <input placeholder="enter player name..." />

    <div class="timer">Timer: {{ countDown }} </div>

    <div class="container">
  <div class="square">
    <pre>{{ gareth }}</pre>
  </div>
  

</div>
<div>
    <a @click="backButton" :disabled="total > 0" class="back" href="#" >&laquo; Back</a>
    <a @click="nextButton" :disabled="total < 19" class="back" href="#">Next &raquo;</a>
    <!-- <p>Total: {{ total }}</p> -->

</div>


</template>

<script>

import axios from 'axios';


 export default {
        data () {
            return {
                countDown: 90,
                gareth: null,
                total: 0,
                holdData: null,
                players : ['Gareth_Barry', 'Ryan_Giggs', 'Frank_Lampard', 'David_James_(footballer,_born_1970)', 'Gary_Speed', 'Emile_Heskey', 'Mark_Schwarzer', 'Sol_Campbell', 'James_Milner', 'Phil_Neville', 'Jamie_Carragher', 'Steven_Gerrard', 'Paul_Scholes', 'Rio_Ferdinand', 'Wayne_Rooney', 'John_Terry', 'Ashley_Cole', 'David_Silva', 'Petr_Čech', 'Cesc_Fàbregas']


            }
        },
        methods: {
            nextButton() {
                if (this.total < 19) {

                    this.total += 1;
                    // console.log(this.players[1])
                    this.gareth = JSON.stringify(this.holdData[this.players[this.total]], null, 2)
                }
            },
            backButton() {
                if (this.total > 0) {
                    this.total -= 1;
                    this.gareth = JSON.stringify(this.holdData[this.players[this.total]], null, 2)
                }

            },
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
                // console.log("hello "+ response.data.data.Gareth_Barry)
                this.holdData =response.data.data
                this.gareth = JSON.stringify(response.data.data.Gareth_Barry, null, 2)
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
   margin-bottom: 10px;

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
    height: 450px;
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
   text-decoration: none;
   color: white;
   background: #dc3545;
   padding: 7px 10px;
   border-radius: 4px;  
   font-size: 19px;
  margin-top: 20px;
}
.nav:hover {
  box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24),0 17px 50px 0 rgba(0,0,0,0.19);
}

pre {
  white-space: pre-wrap;
}

</style>