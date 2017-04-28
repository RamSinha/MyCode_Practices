package com.adobe.publish.service.core.service;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class WorkerService {

    private int MAX_THREAD_COUNT = 10;
    private ExecutorService  executorService;
    private static WorkerService mWorkerService;

    private WorkerService(){
        executorService = Executors.newFixedThreadPool(MAX_THREAD_COUNT);
    }

    public static WorkerService  getWorkerService() {
        if(mWorkerService == null){
            synchronized (WorkerService.class) {
                if(mWorkerService == null){
                    mWorkerService = new WorkerService();
                }
            }
        }
        return  mWorkerService;
    }

    public  <V> Future<V> SubmitTask(Callable<V> task){
        return executorService.submit(task);
    }

    public <V> List<Future<V>> SubmitTask(Collection<Callable<V>> tasks){
         List<Future<V>> list = new ArrayList<Future<V>>();
         for(Callable<V> task: tasks){
            list.add(executorService.submit(task));
         }
        return  list;
    }
}
