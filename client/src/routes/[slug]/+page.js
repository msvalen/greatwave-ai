export async function load ({ params }) {
  let data = await fetch(`http://localhost:8000/location/${params.slug}`)
  let json = await data.json()
  return { data: json, selected: params.slug }
}
