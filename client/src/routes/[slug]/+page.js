import { redirect } from '@sveltejs/kit'

export async function load ({ params }) {
  if (!['london', 'murcia', 'newport', 'paris', 'ny'].includes(params.slug)) {
    redirect(302, '/london')
  }
  const data = await fetch(`http://localhost:8000/location/${params.slug}`)
  const json = await data.json()
  return { data: json, selected: params.slug }
}
