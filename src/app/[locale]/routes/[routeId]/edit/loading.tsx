import LoadingSpinner from '@/app/components/LoadingSpinner'

export default function LoadingPage() {
  return (
    <main className="relative h-[calc(100dvh-65px)] w-full bg-background overflow-hidden">
      <LoadingSpinner />
    </main>
  )
}
