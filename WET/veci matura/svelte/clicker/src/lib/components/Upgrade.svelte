<script>
    import { shared } from "$lib/shared.svelte"
    let {upgradeLevel} = $props()
    let shopClicked = $state(false)

    function adddddd(){
        shopClicked = ! shopClicked
        
        if (upgradeLevel == 1){
            shared.multi = 2
        }if(upgradeLevel == 2){
            shared.multi = 5
        }if(upgradeLevel == 3){
            shared.multi = 10
        }


    }
</script>
<div>
    {#if shopClicked}
        <p>Shop upgrade</p>
    {:else}
        <p>Level {upgradeLevel} upgrade</p>
    {/if}
        <button class="btn" onclick= {adddddd}>Upgrade {upgradeLevel}</button>
</div>
<style>
.btn{
    border: 2px solid black;
    padding: 1em 2em ;
    background-color: rebeccapurple;
    color: white;
    margin-bottom: 10px;
    border-radius: 100px;
    transition: 0.5s linear;
}
.btn:active{
    scale: 0.5;
}
</style>