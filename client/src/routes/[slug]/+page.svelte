<script>
	import { goto } from '$app/navigation';
	export let data;
  const onChange = (e,value) => {
		goto('/'+e.currentTarget.value)
	}
</script>

<main class='py-4' style='height: 100vh; background-image: url("https://source.unsplash.com/random?{data.data.weather[0].main}");  text-align: center;background-repeat:no-repeat;background-size:cover;' >
<div class='container p-4 bg-body-secondary bg-opacity-25 rounded-2'>
  <h1 style='-webkit-text-stroke: 0.05em black; color: white;'>Current weather in {data.data.name}:</h1>
  <h2 style='-webkit-text-stroke: 0.05em #198754; color: white;' > {data.data.weather[0].main} <img src='https://openweathermap.org/img/wn/{data.data.weather[0].icon}@2x.png' alt='Weather icon'/> {data.data.main.temp} ºC</h2>
  <select bind:value={data.selected} class="form-select" aria-label="Select different location" on:change={onChange}>
    <option value="london">London</option>
    <option value="paris">Paris</option>
    <option value="ny">New York</option>
    <option value="newport">Newport (Wales)</option>
    <option value="murcia">Murcia (Spain)</option>
  </select>
</div>
</main>