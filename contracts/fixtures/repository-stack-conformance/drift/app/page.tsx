import { Button as ForeignButton } from "another-ui"
import { FiCheck } from "react-icons/fi"

export default function Page() {
  return (
    <main className="feature-theme">
      <div role="dialog" aria-modal="true" className="local-dialog">
        <label htmlFor="status">Status</label>
        <div id="status" role="listbox" className="local-select">Active</div>
        <ForeignButton><FiCheck />Save</ForeignButton>
      </div>
    </main>
  )
}
