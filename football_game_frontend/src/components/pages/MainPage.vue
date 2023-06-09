<template>
    <div>
        <button class="nav">
            <router-link to="/">Home</router-link>
        </button>
    <h1>Guess the Player</h1>
    </div>

    {{ countDown }}

</template>

<script>
 export default {
        data () {
            return {
                countDown: 10
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
            }
        },
        created () {
            this.countDownTimer()
        }
    }


</script>


<style>


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