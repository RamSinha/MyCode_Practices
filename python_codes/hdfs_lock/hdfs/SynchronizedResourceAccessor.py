from ooziecore.lib.hdfs.HdfsLock import HdfsLock, HdfsLockException
import guavus.glogging.glogger as glogger

class SynchronizedResourceAccessor:
    def __init__(self, lockfile, lock_expiry):
        self.lock = HdfsLock(lockfile, lock_expiry)

    def lock_execute_unlock(self, obj, function_name, *function_args):
        """

        Obtains a lock then executes given function and finally releases lock.
        @param:
            obj: object or module
            function_name: name of the function to be executed. Must be a string.
            function_args: arguments to the function
        @return:
            status: 0 on successful execution 
                    1 on failure
                   -1 on partially successful execution. E.g. given function was executed successfully but error occurred during lock release
            
            result: return value of given function executed on given object
            errors: list of errors occurred during executing the method in order of their occurrence.
                    contains exceptions thrown during the execution

        """

        status,result,errors = 1,'',''
        errors = []
        lockAquired = False
        try:
            lockAquired = self.lock.acquire()
            if lockAquired:
                result = getattr(obj, function_name)(*function_args)
                status = 0
        except Exception as e:
            errors.append(e)
        finally:
            if lockAquired:
                try:
                    self.lock.release()
                except HdfsLockException as e:
                    status = -1 if status == 0 else status
                    errors.append(e)
        if not lockAquired:
            errors.append(Exception('could not acquire lock while executing ' + function_name))
        return status,result,errors

