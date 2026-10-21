import { useState } from 'react'
import { LayoutDashboard, Store, Video, ShieldAlert, Globe, Eye } from 'lucide-react'
import StoreMap3D from './components/StoreMap3D'
import HeatmapView from './components/HeatmapView'
import TheftAlerts from './components/TheftAlerts'

const NAV_ITEMS = [
  { id: 'dashboard', label: 'Dashboard', icon: LayoutDashboard },
  { id: 'lojas', label: 'Lojas', icon: Store },
  { id: 'heatmap', label: 'Heatmap de Atenção', icon: Eye },
  { id: 'alertas', label: 'Alertas de Furto', icon: ShieldAlert },
  { id: 'camera', label: 'Câmeras ao Vivo', icon: Video },
]

export default function App() {
  const [active, setActive] = useState('dashboard')

  return (
    <div className="min-h-screen bg-gray-50 text-slate-900">
      {/* Navbar */}
      <nav className="bg-slate-800 text-white px-6 py-4">
        <div className="max-w-7xl mx-auto flex justify-between items-center">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 bg-cyan-500 rounded-lg flex items-center justify-center">
              <Globe className="w-5 h-5" />
            </div>
            <span className="font-bold text-xl tracking-tight">Synapse 3D</span>
          </div>
          <div className="flex gap-1">
            {NAV_ITEMS.map((item) => (
              <button
                key={item.id}
                onClick={() => setActive(item.id)}
                className={`px-4 py-2 rounded-md text-sm font-medium transition-colors ${
                  active === item.id
                    ? 'bg-cyan-600 text-white'
                    : 'hover:bg-slate-700 text-slate-300'
                }`}
              >
                <item.icon className="w-4 h-4 mr-2" />
                {item.label}
              </button>
            ))}
          </div>
        </div>
      </nav>

      {/* Conteúdo */}
      <main className="max-w-7xl mx-auto p-6">
        {active === 'dashboard' && <DashboardView />}
        {active === 'lojas' && <div className="p-4">Em breve: gestão de lojas</div>}
        {active === 'heatmap' && <HeatmapView />}
        {active === 'alertas' && <TheftAlerts />}
        {active === 'camera' && <div className="p-4">Em breve: transmissão ao vivo</div>}
      </main>

      {/* Visualização 3D flutuante (overlay opcional) */}
      <div className="fixed bottom-6 right-6 w-96 h-96 bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden z-50">
        <div className="bg-slate-800 text-white px-3 py-2 flex justify-between items-center">
          <span className="text-sm font-semibold">Vista 3D - Loja Matriz</span>
          <button className="text-xs bg-cyan-600 text-white px-2 py-1 rounded">Tela cheia</button>
        </div>
        <StoreMap3D />
      </div>
    </div>
  )
}

function DashboardView() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      {[1, 2, 3, 4].map((i) => (
        <div key={i} className="bg-white p-6 rounded-xl shadow border border-gray-100">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-gray-500 text-sm">Lojas Ativas</p>
              <p className="text-2xl font-bold">40</p>
            </div>
            <div className="w-10 h-10 rounded-full bg-cyan-100 flex items-center justify-center text-cyan-600">
              <Store className="w-5 h-5" />
            </div>
          </div>
        </div>
      ))}
    </div>
  )
}
