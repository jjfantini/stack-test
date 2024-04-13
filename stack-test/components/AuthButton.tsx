"use client"
import { deleteCookie } from 'cookies-next'
import { useRouter } from 'next/navigation'
import Link from "next/link";

type Props = {
  loggedUser?: string
}

export default function AuthButton(props: Props) {
  const { loggedUser } = props
  const router = useRouter()

  const logout = () => {
    deleteCookie('token')
    router.replace('/login')
  }

  return loggedUser ? (
    <div className="flex items-center gap-4">
      Hey, {loggedUser}!
      <button onClick={logout} className="py-2 px-4 rounded-md no-underline bg-btn-background hover:bg-btn-background-hover">
        Logout
      </button>
    </div>
  ) : (
    <Link
      href="/login"
      className="py-2 px-3 flex rounded-md no-underline bg-btn-background hover:bg-btn-background-hover"
    >
      Login
    </Link>
  );
}
