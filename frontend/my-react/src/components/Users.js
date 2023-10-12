import React, { useEffect, useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import UserEditModal from './UserEditModal';

function GetUsers() {
  /*
    El hook userState permite agregar un estado a un componente funcional,
    en este caso "users" es el estado y "setUsers" el método para actualizar dicho estado.
  */
  const [users, setUsersState] = useState([]);
  

  /*
    Dentro de useEffect se ejecutará una sola vez cuando el componente se monte (porque no tiene dependencias añadidas), 
    lo que significa que realizará la solicitud GET al servidor y actualizará el estado users con los datos obtenidos.
  */
  useEffect(() => {
    // Realiza una solicitud GET al backend para obtener la lista de usuarios
    axios.get('http://localhost:8000/user')
    .then(response => 
      { // la variable response contiene los objetos User recogidos por la solicitud http.

        // La función map, mapea los objetos para almacenarlos como filas html (también se ha aplicado boostrap).
        const arrayHtmlUsers = response.data.map(user => 
          <tr scope="row" key={user.id}>
            <td>{user.email}</td>
            <td>{user.name}</td>
            <td>{user.age}</td>
            <td>{user.length}</td>
            <td>{user.weight}</td>
            <td><button type="button" class="btn btn-outline-warning">Editar</button></td>
            <td><button type="button" class="btn btn-outline-danger">Eliminar</button></td>
          </tr>
        )

        // Guardamos la variable con todas sus modificaciones y la añadimos al estado 'users' mediante la función setUserState.
        setUsersState(arrayHtmlUsers);
        console.log(response.data)
      }
    ).catch(error => {
        console.error('Error fetching users:', error);
      });
  },
  []);

  return (
    <div class="float-lg-end">
      <table class="table table-striped">
        <thead>
          <tr>
            <th scope="col">Email</th>
            <th scope="col">Name</th>
            <th scope="col">Age</th>
            <th scope="col">Length</th>
            <th scope="col">Weight</th>
            <th scope="col">Options</th>
          </tr>
        </thead>
        <tbody>
          {users}
        </tbody>
      </table>
    </div>
  );

  }

export default GetUsers;