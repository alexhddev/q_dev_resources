import { useState, useEffect, useCallback } from 'react'
import './App.css'

type Position = { x: number; y: number }
type Direction = 'UP' | 'DOWN' | 'LEFT' | 'RIGHT'

const GRID_SIZE = 20
const INITIAL_SNAKE = [{ x: 10, y: 10 }]
const INITIAL_FOOD = { x: 15, y: 15 }

function App() {
  const [snake, setSnake] = useState<Position[]>(INITIAL_SNAKE)
  const [food, setFood] = useState<Position>(INITIAL_FOOD)
  const [direction, setDirection] = useState<Direction>('RIGHT')
  const [gameOver, setGameOver] = useState(false)
  const [score, setScore] = useState(0)

  const generateFood = useCallback(() => {
    return {
      x: Math.floor(Math.random() * GRID_SIZE),
      y: Math.floor(Math.random() * GRID_SIZE)
    }
  }, [])

  const moveSnake = useCallback(() => {
    if (gameOver) return

    setSnake(currentSnake => {
      const newSnake = [...currentSnake]
      const head = { ...newSnake[0] }

      switch (direction) {
        case 'UP': head.y -= 1; break
        case 'DOWN': head.y += 1; break
        case 'LEFT': head.x -= 1; break
        case 'RIGHT': head.x += 1; break
      }

      // Wrap through walls
      head.x = (head.x + GRID_SIZE) % GRID_SIZE
      head.y = (head.y + GRID_SIZE) % GRID_SIZE

      if (newSnake.some(segment => segment.x === head.x && segment.y === head.y)) {
        setGameOver(true)
        return currentSnake
      }

      newSnake.unshift(head)

      if (head.x === food.x && head.y === food.y) {
        setFood(generateFood())
        setScore(s => s + 1)
      } else {
        newSnake.pop()
      }

      return newSnake
    })
  }, [direction, food, gameOver, generateFood])

  useEffect(() => {
    const handleKeyPress = (e: KeyboardEvent) => {
      switch (e.key) {
        case 'ArrowUp': setDirection('UP'); break
        case 'ArrowDown': setDirection('DOWN'); break
        case 'ArrowLeft': setDirection('LEFT'); break
        case 'ArrowRight': setDirection('RIGHT'); break
      }
    }
    window.addEventListener('keydown', handleKeyPress)
    return () => window.removeEventListener('keydown', handleKeyPress)
  }, [])

  useEffect(() => {
    const gameInterval = setInterval(moveSnake, 150)
    return () => clearInterval(gameInterval)
  }, [moveSnake])

  const resetGame = () => {
    setSnake(INITIAL_SNAKE)
    setFood(INITIAL_FOOD)
    setDirection('RIGHT')
    setGameOver(false)
    setScore(0)
  }

  return (
    <div className="game">
      <h1>Snake Game</h1>
      <div className="score">Score: {score}</div>
      {gameOver && (
        <div className="game-over">
          <div>Game Over!</div>
          <button onClick={resetGame}>Play Again</button>
        </div>
      )}
      <div className="grid">
        {Array.from({ length: GRID_SIZE * GRID_SIZE }).map((_, index) => {
          const x = index % GRID_SIZE
          const y = Math.floor(index / GRID_SIZE)
          const isSnake = snake.some(segment => segment.x === x && segment.y === y)
          const isFood = food.x === x && food.y === y
          return (
            <div
              key={index}
              className={`cell ${isSnake ? 'snake' : ''} ${isFood ? 'food' : ''}`}
            />
          )
        })}
      </div>
      <div className="controls">
        Use arrow keys to control the snake
      </div>
    </div>
  )
}

export default App
