import $ from 'jquery';

const ModuleTutor = {
    namespaced: true,
    state: {
        id: '',
        username: '',
        photo: '',
        is_login: false,
        college: '',
        date_of_birth: '',
        gender: '',
        research_area: '',
        bio: '',
        email: '',
        phone: '',
        is_recruiting_specialized: false,
        is_recruiting_learning: false,
        enrollment_limit: 0,
        enrollment_count: 0,
        user: ''
  },
  getters: {
  },
  mutations: {
        updateTutor(state, tutor) {
            state.id = tutor.id;
            state.username = tutor.username;
            state.photo = tutor.photo;
            state.college = tutor.college;
            state.date_of_birth = tutor.date_of_birth;
            state.gender = tutor.gender;
            state.research_area = tutor.research_area;
            state.bio = tutor.bio;
            state.email = tutor.email;
            state.phone = tutor.phone;
            state.is_recruiting_specialized = tutor.is_recruiting_specialized;
            state.enrollment_limit =  tutor.enrollment_limit;
            state.enrollment_count = tutor.enrollment_count;
        },
      logout(state) {
            state.id = '';
            state.username = '';
            state.photo = '';
            state.college = '';
            state.data_of_birth = '';
            state.gender = '';
            state.student_type = '';
            state.bio = '';
            state.email = '';
            state.phone = '';
            state.is_selected = '';
            state.select_limit =  '';
            state.select_count = '';
            state.tutor_id = '';
            state.tutor_name = '';
            state.is_login = false;
            state.user = '';
      }
  },
  actions: {
        get_info(context) {
            context.state.is_login = true;
            $.ajax({
                url: 'http://8.130.65.99:8002/tutor/get_info/',
                type: 'GET',
                data: {
                    user: context.state.user,
                },
                success(resp) {
                    if (resp.result === 'success') {
                        context.commit('updateTutor', resp.date);
                    }
                }
            })
        },
      logout(context) {
            context.commit('logout')
      }
  },
  modules: {
  }
};
export default ModuleTutor;