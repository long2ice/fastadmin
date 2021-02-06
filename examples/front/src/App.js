import * as React from "react";
import simpleRestProvider from 'ra-data-simple-rest';
import {Admin, Resource} from 'react-admin';
import {UserList, UserCreate, UserEdit, UserShow} from './user';
import AuthProvider from './authProvider';
import LoginPage from './login';

const dataProvider = simpleRestProvider('http://127.0.0.1:8000/admin');
const App = () => (
    <Admin dataProvider={dataProvider}  loginPage={LoginPage} authProvider={AuthProvider}>
        <Resource name="user" list={UserList} show={UserShow} create={UserCreate} edit={UserEdit}/>
    </Admin>
);
export default App;
