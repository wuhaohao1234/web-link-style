import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '^/get_url': {
        target: 'http://localhost:8383',
        changeOrigin: true,
      }
    }
  }
})
