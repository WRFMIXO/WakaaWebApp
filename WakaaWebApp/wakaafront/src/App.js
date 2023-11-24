import './App.css';
import { BrowserRouter, Routes, Route} from 'react-router-dom';
import AdminLoginPage from './components/commons/AdminLoginPage';
import UserLoginPage from './components/commons/UsersLoginPage';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path='/administration/login' element={<AdminLoginPage/>} />
          <Route path='/entreprises/login' element={<UserLoginPage />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
