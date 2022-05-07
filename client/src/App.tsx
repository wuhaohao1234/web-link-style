import { useState } from 'react'
import './App.css'

function App() {
  const [desc, setDesc] = useState({title: '', desc: '', url: ''})
  const [value, setValue] = useState('')
  const getDescByValue = () => {
    fetch(`get_url?url=${value}`).then(res => {
      return res.json()
    }).then(res => {
      setDesc(res)
    })
  }
  const handleChange = (value: any) => {
    setValue(value.target.value)
  }
  return (
    <div className="App">
      <input type="text" onChange={handleChange} value={value} />
      <button onClick={getDescByValue} >确认</button>
      <p>请输入语雀某一篇文章链接例如: https://www.yuque.com/shenweiyan/cookbook/r-packages-guide</p>
      <h1>
        {desc.title}
      </h1>
      <p>
        {desc.desc}
      </p>
      <a href={desc.url}>{desc.title}</a>
    </div>
  )
}

export default App
