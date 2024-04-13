import axios from 'axios'
const client = axios.create({
  baseURL: process.env.NEXT_PUBLIC_FAST_API_URL
})

export const login = async (email: string, password: string) => {
  const { data } = await client.post('/login', {
    email,
    password
  })
  return data
}

export const register = async (email: string, password: string) => {
  const { data } = await client.post('/register', {
    email,
    password
  })
  return data
}

export const getUser = async (token: string) => {
  const { data } = await client.get('/user', {
    headers: {
      Authorization: "Bearer " + token
    }
  })
  return data
}
