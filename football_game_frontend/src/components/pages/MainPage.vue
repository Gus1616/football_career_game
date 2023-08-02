<template>
    <div>
        <button class="nav">
            <router-link class="routerLink" style="text-decoration: none;" to="/">Home</router-link>
        </button>
    <h1>Guess the Player</h1>
    </div>
    <input class="inputBox" type="text" v-model="inputText" placeholder="enter player name..." />

    <div class="timer">
        <div class="timerDiv">
            <div>Timer: {{ countDown }} </div>
        </div>
        <div class="ScoreDiv">
            <div>Total Score: {{ totalScore }} </div>
        </div>

    </div>

    


    <div class="container">
            <div class="square">
                <!-- <pre>{{ gareth }}</pre> -->
                <p v-html="gareth"></p>
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
import { useStore } from 'vuex';


 export default {
        data () {
            return {
                inputText: "",
                totalScore: 0,

                countDown: 90,
                gareth: null,
                total: 0,
                holdData: null,
                players : ['Gareth_Barry', 'Ryan_Giggs', 'Frank_Lampard', 'David_James_(footballer,_born_1970)', 'Gary_Speed', 'Emile_Heskey', 'Mark_Schwarzer', 'Sol_Campbell', 'James_Milner', 'Phil_Neville', 'Jamie_Carragher', 'Steven_Gerrard', 'Paul_Scholes', 'Rio_Ferdinand', 'Wayne_Rooney', 'John_Terry', 'Ashley_Cole', 'David_Silva', 'Petr_Čech', 'Cesc_Fàbregas']


            }
        },
        setup() {
                const store = useStore();

                const sendDataToSibling = () => {
                const data = this.score ;
                store.commit('updateData', data);
                };

                return {
                sendDataToSibling,
                };
        },
        methods: {
            loadFinalScore() {
      const finalScore = localStorage.getItem('finalScore');
      if (finalScore) {
        this.totalScore = parseInt(finalScore);
      }
    },
    saveFinalScore() {
      localStorage.setItem('finalScore', this.totalScore);
      console.log("saving final score ", this.totalScore)
    },
            
            nextButton() {
                if (this.total < 19) {

                    this.total += 1;
                    // console.log(this.players[this.total])
                    let jsonData = this.holdData[this.players[this.total]]
                    let newVarrr = jsonData.map((item) => item.replace(/\[\d+\]/g, ""));
                    // console.log("hello json data "+jsonData)
                    newVarrr =  newVarrr.join("<br>");

                    
                    this.gareth = newVarrr
                    // this.gareth = JSON.stringify(this.holdData[this.players[this.total]], null, 2)
                    
                }
            },
            backButton() {
                if (this.total > 0) {
                    this.total -= 1;
                    let jsonData = this.holdData[this.players[this.total]]
                    let newVarrr = jsonData.map((item) => item.replace(/\[\d+\]/g, ""));
                    newVarrr =  newVarrr.join("<br>");

                    
                    this.gareth = newVarrr
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
        computed: {
        },
        watch: {
                inputText(newInput) {
                this.displayedText = newInput;
                let stringRepresentation = this.players[this.total].toString();
                // console.log("thisss string " + stringRepresentation)


                if (newInput === stringRepresentation) {
                    this.totalScore += 1;
                    this.total += 1;
                    this.inputText = "";
                    //                 const store = useStore();
                    // store.commit('updateData', this.totalScore);


                    this.$store.commit('updateData', this.totalScore);


                    // console.log(this.players[this.total])
                    this.gareth = JSON.stringify(this.holdData[this.players[this.total]], null, 2)
                }
                },
                score(newScore) {
                        // Save the score to the browser's local storage whenever it changes
                        localStorage.setItem('gameScore', newScore);
                        console.log("Emitted newscore: "+ newScore)

                        // Emit the custom event with the score value
                        this.$emit('score-updated', newScore);
            },
         },
        created () {
            this.countDownTimer(),
            axios.get('http://localhost:8000/careerApp/load-json/')
            .then(response => {
                // this.message = response.data.message;
                // console.log("hello "+ response.data.data.Gareth_Barry)
                this.holdData =response.data.data
                let jsonDataa = response.data.data.Gareth_Barry
                let newVar = jsonDataa.map((item) => item.replace(/\[\d+\]/g, ""));
                newVar =  newVar.join("<br>");
                // console.log(newVar)

                
                this.gareth = newVar
            })
            .catch(error => {
                console.error(error);
            });
            

            this.loadFinalScore();
             window.addEventListener('beforeunload', this.saveFinalScore);
                    
        },
        beforeUnmount() {
    window.removeEventListener('beforeunload', this.saveFinalScore);
  },

        


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
  right: 40px;
  font-size: 30px;

}

.routerLink{
    text-decoration: none;
    color: white;
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

.inputBox{
    box-shadow:4px 4px 10px rgba(0,0,0,0.06);
    border-radius:10px;
    padding:4px;
    height: 25px;
    width: 350px;


}

.timerDiv{
    border: 4px solid red;
    padding: 2px;
    border-radius:5px;
    box-shadow:4px 4px 10px rgba(0,0,0,0.06);



}

.ScoreDiv{
    border: 4px solid green;
    border-radius:5px;
    padding: 2px;
    margin-top: 12px;
    box-shadow:4px 4px 10px rgba(0,0,0,0.06);



}

</style>