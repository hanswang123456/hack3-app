const inputEl = document.querySelector(".search_text")

document.addEventListener("click", e => {
  if (!e.target.closest(".search_container")) return
  inputEl.focus()
})
