import {combineReducers, createStore, compose, applyMiddleware } from 'redux';
import { scheduleListReducer } from './reducers/scheduleReducers';
import { thunk } from 'redux-thunk'


const reducer = combineReducers({
    scheduleList: scheduleListReducer,
})

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const middleware = [thunk]

export const store = createStore(reducer, composeEnhancers(applyMiddleware(...middleware)))