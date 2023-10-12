import React from 'react';

const UserEditModal = (props) => {
  // Contenido del modal aquí
  return (
    <div className="modal">
      {/* Contenido del modal */}
      <div className="modal-content">
        {/* Aquí puedes colocar los campos de edición de usuario */}
        {props.children}
      </div>
    </div>
  );
};

export default UserEditModal;