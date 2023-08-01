import { createStore } from 'vuex';

const store = createStore({
  state() {
    return {
      data: '',
    };
  },
  mutations: {
    updateData(state, newData) {
      state.data = newData;
    },
  },
});

export default store;

