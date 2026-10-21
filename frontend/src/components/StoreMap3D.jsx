import { useRef, useState } from 'react'
import { Canvas } from '@react-three/fiber'
import { OrbitControls, Grid, AxesHelper } from '@react-three/drei'

export default function StoreMap3D() {
  const [hovered, setHovered] = useState(null)

  return (
    <Canvas shadows camera={{ position: [5, 5, 5], fov: 45 }}>
      <OrbitControls enablePan={false} makeDefault />
      <Grid args={[10, 10]} />
      <AxesHelper />

      {/* Prateleira da loja (representação simplificada) */}
      <mesh
        onClick={(e) => setHovered('prateleira-medicamentos')}
        onPointerOver={(e) => setHovered('prateleira-medicamentos')}
        onPointerOut={(e) => setHovered(null)}
      >
        <boxGeometry args={[2, 1.5, 0.3]} />
        <meshStandardMaterial color="#e2e8f0" />
      </mesh>

      <pointLight position={[10, 10, 10]} />
      <ambientLight intensity={0.5} />
    </Canvas>
  )
}
