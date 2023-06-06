<template>
    <a-card title="Default size card" style="width: 300px">
      <template #extra><div @click="open_tutor_info(tutor_id)">more</div></template>
      <p>姓名：{{ name }}</p>
      <p>性别：{{ gender }}</p>
      <p>研究方向：{{ research }}</p>
    </a-card>
    <br />
</template>


<script>
import router from '@/router/index';
export default ({
    name: "PersonInfo",
    props: {
        name: {
            type: String,
            default: "default"
        },
        gender: {
            type: String,
            default: "default"
        },
        research: {
            type: String,
            default: "default"
        },
        tutor_id: {
            type: String,
            default: 'default',
        }

    },
    setup() {
        const open_tutor_info = id => {
            console.log(id);
            router.push({
                name: 'looktutorinfo',
                params: {
                    tutorid: id
                }
            })
        }
        return {
            open_tutor_info
        }
    }
})
</script>