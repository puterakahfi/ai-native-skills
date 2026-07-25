import { Check } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"

export default function Page() {
  return (
    <main className="mx-auto max-w-3xl space-y-6 px-6 py-12">
      <h1 className="text-page-title">Repository-native controls</h1>
      <Select defaultValue="active">
        <SelectTrigger aria-label="Member status">
          <SelectValue placeholder="Choose status" />
        </SelectTrigger>
        <SelectContent>
          <SelectItem value="active">Active</SelectItem>
          <SelectItem value="paused">Paused</SelectItem>
        </SelectContent>
      </Select>
      <Button variant="outline"><Check className="mr-2 size-4" aria-hidden="true" />Save</Button>
    </main>
  )
}
