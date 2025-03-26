<script>

    import {shared} from "$lib/shared.svelte";

</script>

<button class="btn" onclick={(() => {
    setInterval(() => {
        shared.count++
    }, 1000)
})}> AUTOCLICKER </button>

<style>

    .btn {
        border: 2px solid black;
        padding: 1em 2em;
        border-radius: 5000px;
        background-color: rgb(99, 176, 199);
        color: white;
    }
</style>
