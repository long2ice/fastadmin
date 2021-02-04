import * as React from "react";
import jsonServerProvider from 'ra-data-json-server';
import {Admin, Resource} from 'react-admin';
import {UserList} from './users';

const dataProvider = jsonServerProvider('http://127.0.0.1:8000/admin');
const App = () => (
    <Admin dataProvider={dataProvider}>
        <Resource name="users" list={UserList}/>
    </Admin>
);
export default App;
