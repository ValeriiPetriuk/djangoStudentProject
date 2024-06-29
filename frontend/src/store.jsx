import {combineReducers, createStore, compose, applyMiddleware } from 'redux';
import { scheduleListReducer } from './reducers/scheduleReducers';
import { thunk } from 'redux-thunk'
import { groupsListReducer } from './reducers/groupReducers';


const reducer = combineReducers({
    scheduleList: scheduleListReducer,
    groupsList: groupsListReducer,
})

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const middleware = [thunk]

export const store = createStore(reducer, composeEnhancers(applyMiddleware(...middleware)))