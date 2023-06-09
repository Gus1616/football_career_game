<template>
    <div>
        <button class="nav">
            <router-link to="/">Home</router-link>
        </button>
    <h1>Guess the Player</h1>
    </div>

    <div class="timer">Timer: {{ countDown }}</div>

</template>

<script>
 export default {
        data () {
            return {
                countDown: 25
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
            this.countDownTimer()
        }
    }


</script>


<style>

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