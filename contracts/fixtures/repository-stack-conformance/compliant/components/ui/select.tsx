import * as SelectPrimitive from "@radix-ui/react-select"
import { ChevronDown } from "lucide-react"
import { cn } from "@/lib/utils"

export const Select = SelectPrimitive.Root
export const SelectValue = SelectPrimitive.Value

export function SelectTrigger({ className, children }: SelectPrimitive.SelectTriggerProps) {
  return (
    <SelectPrimitive.Trigger className={cn("flex h-10 items-center justify-between rounded-md border bg-background px-3", className)}>
      {children}
      <ChevronDown className="size-4" aria-hidden="true" />
    </SelectPrimitive.Trigger>
  )
}

export function SelectContent({ children }: SelectPrimitive.SelectContentProps) {
  return <SelectPrimitive.Content className="rounded-md border bg-popover p-1">{children}</SelectPrimitive.Content>
}

export const SelectItem = SelectPrimitive.Item
