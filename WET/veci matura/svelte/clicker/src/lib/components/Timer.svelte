<script>
    let elapsedTime = $state(0)
    $effect(()=>{
        setInterval(()=> {
        elapsedTime++
        },1000)
    })
    
</script>

<p> Timer: {elapsedTime}</p>