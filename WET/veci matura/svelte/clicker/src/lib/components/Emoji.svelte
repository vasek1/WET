<script>

import {shared} from "$lib/shared.svelte"
let randomPosition = Math.floor(Math.random()*10)+1


</script>

<button class="btn" onclick={(() => {shared.count += Math.floor((Math.random() * 10) + 1), style="--pozice:{randomPosition}"})}> Emoji </button>


<style>

    .btn {
        border: 2px solid black;
        padding: 1em 2em;
        border-radius: 5000px;
        background-color: rgb(150, 190, 19);
        color: white;
        position: var(--pozice, absolute);
        margin-top: 400px;
    }
</style>
