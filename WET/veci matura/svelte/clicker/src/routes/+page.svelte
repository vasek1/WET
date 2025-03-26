<script>
	import Timer from "$lib/components/Timer.svelte"
    import Upgrade from "$lib/components/Upgrade.svelte"
    import Emoji from "$lib/components/Emoji.svelte"
    import Autoclicker from "$lib/components/Autoclicker.svelte"
    import { shared} from "$lib/shared.svelte"
	

    let count = $state(0)
    let animPop = $state()
    let ha = $state()
    let podvod = ""

    function pridej(){
        shared.count = shared.count + shared.multi 
        ha ="anim-but"
        setTimeout(()=>{
            ha = ""
        }, 100)
    }

    $effect(()=> {
        if (shared.count>0){
            animPop = "anim-pop"
        }
        setTimeout(()=>{
            animPop = ""
        }, 100)
    })
    function cheat(){
        if(input === "janes"){
            shared.count += 1000
            podvod = cheat
        }
            
    }
</script>
<Emoji/>
<Timer/>
    
<Upgrade upgradeLevel ={1}/>
<Upgrade upgradeLevel ={2}/>
<Upgrade upgradeLevel ={3}/>

<div class="wrapper">
    
    <p class={animPop}>{shared.count}</p>
<button class ="btn {ha}" onclick={pridej}>Click me!</button>

<Autoclicker/>

<input type="text"class="input" bind:value={podvod}>
</div>


<style>
    .wrapper{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        min-height: 100vh;
        gap: 1em;
        
    }
    .input {
        padding: 0.5em;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 1em;
    }
    .btn{
        
        border: 2px solid black;
        padding: 1em 2em ;
        border-radius: 500px;
        background-color: rebeccapurple;
        color: white;
    }
    .anim-pop{
        animation: popout  0.1s;
    }
    .anim-but{
        animation: butanim 0.1s;
    }

    @keyframes popout{
        50%{
            scale: 2;
        }
        100%{
            scale: 1;
        }
    }
    @keyframes butanim{
        100%{
            scale: 0.95;
        }
        50%{
            scale: 1;
        }
    }
</style>