import Head from 'next/head'
import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
    <>
      <Head>
        <title>Create Next App</title>
        <meta name="description" content="Generated by create next app" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <div className=' sm:w-[90%]  mx-auto h-[50%]'>
        <iframe className=' w-full h-full' src="http://localhost:3000/d-solo/en2yCsa4k/overview-of-devices?orgId=1&panelId=2&kiosk"></iframe>
      </div>
    </>
  )
}
