import React, { useState, useEffect } from 'react';
import { Container, Carousel, Button, Dropdown, Form, DropdownButton, FormGroup } from 'react-bootstrap';
import '../../assets/css/AdminLoginPage.css';

const AdminLoginPage = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [carousel, setCarousel] = useState({
        title: "",
        description: "",
    });
    const [rememberMe, setRememberMe] = useState(false);

    const handleLogin = async(e) => {
        e.preventDefault();
        // Logique pour gérer la connexion
        try{
            // Envoyer les données d'authentification au backend Django
            const response = await fetch('http://localhost:8000/administration/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    email,
                    password,
                    rememberMe,
                }),
            });

            if(response.ok) {
                // Connexion réussie, rediriger l'utilisateur ou effectuer d'autres actions nécessaires
                console.log('Connexion Réussie !');
            } else {
                // Gérer les erreurs d'authentification ici
                console.error("Echec de la connexion");
            }
        } catch (error) {
            console.error('Erreur lors de la connexion', error);
        }
    };

    const handleCheckboxChange = () => {
        setRememberMe(!rememberMe);
      };

    return(
        <div>
        <div className="container-fluid mt-5">
            <div className="row justify-content-center align-items-center" id='formCarouselRow'>
          {/* Colonne de gauche avec le formulaire */}
          <div className="col-md-6">
            <main className="form-signin">
              <form style={{textAlign: "center"}}>
                <img
                  src="../../assets/images/cars-5970663_1920.png"
                  className="mb-4"
                  alt=""
                  width="100"
                  height="80"
                />
                
                <h1 className='label-connexion'>Connectez-vous</h1>
                <h3 className='label-administration'>Administration</h3>

                <Form.Group controlId="inputEmail" className="mb-3">
                  <Form.Label className='visually-hidden'>Adresse Email :</Form.Label>
                  <Form.Control
                    type="email"
                    placeholder="Entrez votre adresse email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                    autoFocus
                    className='form-control'
                  />
                </Form.Group>
  
                <Form.Group controlId="inputPassword" className="mb-3">
                  <Form.Label className='visually-hidden'>Mot de passe :</Form.Label>
                  <Form.Control
                    type="password"
                    placeholder="Entrez votre mot de passe"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                    autoFocus
                    className='form-control'
                  />
                </Form.Group>

                <Form.Group controlId="rememberMe" className="mb-3">
                    <Form.Check
                        type="checkbox"
                        label="Se souvenir de moi"
                        checked={rememberMe}
                        onChange={handleCheckboxChange}
                        style={{textAlign:"left"}}
                />
              </Form.Group>
  
                <Button variant="primary" type="submit" onClick={handleLogin} className='submit'>
                  Sign in
                </Button>
                <hr />
              </form>
            </main>
          </div>
  
          {/* Colonne de droite avec le carrousel */}
          <div className="col-md-6" id='carousel'>
            <Carousel>
              <Carousel.Item>
                <img
                  className="d-block w-100"
                  src="https://via.placeholder.com/800x600"
                  alt="First slide"
                />
                <Carousel.Caption>
                  <h3>Image 1</h3>
                </Carousel.Caption>
              </Carousel.Item>

              <Carousel.Item>
                <img
                  className="d-block w-100"
                  src="https://via.placeholder.com/800x600"
                  alt="First slide"
                />
                <Carousel.Caption>
                  <h3>Image 2</h3>
                </Carousel.Caption>
              </Carousel.Item>

              <Carousel.Item>
                <img
                  className="d-block w-100"
                  src="https://via.placeholder.com/800x600"
                  alt="First slide"
                />
                <Carousel.Caption>
                  <h3>Image 3</h3>
                </Carousel.Caption>
              </Carousel.Item>

              <Carousel.Item>
                <img
                  className="d-block w-100"
                  src="https://via.placeholder.com/800x600"
                  alt="First slide"
                />
                <Carousel.Caption>
                  <h3>Image 4</h3>
                </Carousel.Caption>
              </Carousel.Item>
              {/* Ajoutez autant d'items de carrousel que nécessaire */}
            </Carousel>
          </div>
        </div>
      </div>

        <div className='row' id='footer'>
            <div className='col'>
                <p>&copy; Waka'a. All Rights Reserved</p>
            </div>
            <div className='col'>
            </div>
            <div className='col'>
                <p>Provided and promoted by <a href="https://www.akc-invent.cm" >AKC-Invent</a></p>
            </div>
        </div>
    </div>
    );
};

export default AdminLoginPage;