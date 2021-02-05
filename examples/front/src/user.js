import * as React from "react";
import {
    List,
    Datagrid,
    TextField,
    ImageField,
    Pagination,
    DateField,
    Filter,
    TextInput,
    BooleanField,
    Show,
    SimpleShowLayout,
    Create,
    Edit,
    SimpleForm,
    useListContext,
    TopToolbar,
    CreateButton,
    ExportButton,
    sanitizeListRestProps, DateTimeInput, BooleanInput
} from 'react-admin';

import {cloneElement} from 'react';

const PostFilter = (props) => (
    <Filter {...props}>
        <TextInput label="Search Username" source="username" alwaysOn/>
    </Filter>
);
const PostPagination = props => <Pagination rowsPerPageOptions={[10, 25, 50, 100]} {...props} />;
const ListActions = (props) => {
    const {
        className,
        exporter,
        filters,
        maxResults,
        ...rest
    } = props;
    const {
        currentSort,
        resource,
        displayedFilters,
        filterValues,
        hasCreate,
        basePath,
        selectedIds,
        showFilter,
        total,
    } = useListContext();
    return (
        <TopToolbar className={className} {...sanitizeListRestProps(rest)}>
            {filters && cloneElement(filters, {
                resource,
                showFilter,
                displayedFilters,
                filterValues,
                context: 'button',
            })}
            <CreateButton basePath={basePath}/>
            <ExportButton
                disabled={total === 0}
                resource={resource}
                sort={currentSort}
                filterValues={filterValues}
                maxResults={maxResults}
            />
        </TopToolbar>
    );
};
export const UserList = props => (
    <List {...props} filters={<PostFilter/>} pagination={<PostPagination/>} actions={<ListActions/>}>
        <Datagrid rowClick="edit">
            <TextField source="id"/>
            <TextField source="username"/>
            <BooleanField source="is_active"/>
            <BooleanField source="is_superuser"/>
            <DateField source="last_login"/>
            <ImageField source="avatar"/>
            <TextField source="intro"/>
            <DateField source="created_at"/>
        </Datagrid>
    </List>
);
export const UserShow = (props) => (
    <Show {...props}>
        <SimpleShowLayout>
            <TextField source="id"/>
            <TextField source="username"/>
            <BooleanField source="is_active"/>
            <BooleanField source="is_superuser"/>
            <DateField source="last_login"/>
            <ImageField source="avatar"/>
            <TextField source="intro"/>
            <DateField source="created_at"/>
        </SimpleShowLayout>
    </Show>
);
export const UserCreate = (props) => (
    <Create {...props}>
        <SimpleForm>
            <TextInput source="username"/>
            <BooleanInput source="is_active"/>
            <BooleanInput source="is_superuser"/>
            <DateTimeInput source="last_login"/>
            <TextInput source="avatar"/>
            <TextInput source="intro"/>
            <TextInput source="password"/>
        </SimpleForm>
    </Create>
);
export const UserEdit = (props) => (
    <Edit {...props}>
        <SimpleForm>
            <TextInput source="username"/>
            <BooleanInput source="is_active"/>
            <BooleanInput source="is_superuser"/>
            <DateTimeInput source="last_login"/>
            <TextInput source="avatar"/>
            <TextInput source="intro"/>
            <TextInput source="password"/>
        </SimpleForm>
    </Edit>
);
